from django.shortcuts import render, redirect, get_object_or_404
from .models import Event, Participant, Category
from .forms import EventForm, ParticipantForm, CategoryForm
from django.db.models import Count, Prefetch, Q
from django.db.models import Sum
from django.utils import timezone
from datetime import date

def dashboard(request):
    now = timezone.localdate()
    total_events = Event.objects.count()
    total_participants = Participant.objects.aggregate(total=Count('id'))['total'] or 0
    upcoming_events = Event.objects.filter(date__gte=now).count()
    past_events = Event.objects.filter(date__lt=now).count()
    todays_events = Event.objects.filter(date=now)

    stat_type = request.GET.get('stat_type', 'all')
    if stat_type == 'upcoming':
        list_events = Event.objects.filter(date__gte=now)
    elif stat_type == 'past':
        list_events = Event.objects.filter(date__lt=now)
    else:
        list_events = Event.objects.all()
    context = {
        "total_events": total_events,
        "total_participants": total_participants,
        "upcoming_events": upcoming_events,
        "past_events": past_events,
        "todays_events": todays_events,
        "list_events": list_events,
        "active_stat": stat_type
    }
    return render(request, 'events/dashboard.html', context)

def event_list(request):
    queryset = Event.objects.select_related('category').prefetch_related('participants')
    category_id = request.GET.get('category')
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    if category_id:
        queryset = queryset.filter(category_id=category_id)
    if start_date and end_date:
        queryset = queryset.filter(date__range=[start_date, end_date])
    search = request.GET.get('search', '')
    if search:
        queryset = queryset.filter(Q(name__icontains=search) | Q(location__icontains=search))
    total_participants = Participant.objects.aggregate(total=Count('id'))['total'] or 0
    context = {
        'events': queryset,
        'categories': Category.objects.all(),
        'total_participants': total_participants,
        'search': search,
    }
    return render(request, 'events/event_list.html', context)

def event_detail(request, pk):
    event = get_object_or_404(
        Event.objects.select_related('category').prefetch_related('participants'),
        pk=pk
    )
    return render(request, 'events/event_detail.html', {'event': event})

def event_create(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('event_list')
    else:
        form = EventForm()
    return render(request, 'events/event_form.html', {'form': form, 'action': 'Create'})

def event_update(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('event_detail', pk=pk)
    else:
        form = EventForm(instance=event)
    return render(request, 'events/event_form.html', {'form': form, 'action': 'Update'})

def event_delete(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        event.delete()
        return redirect('event_list')
    return render(request, 'events/event_confirm_delete.html', {'event': event})

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'events/category_list.html', {'categories': categories})

def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm()
    return render(request, 'events/category_form.html', {'form': form, 'action': 'Create'})

def category_update(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'events/category_form.html', {'form': form, 'action': 'Update'})

def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('category_list')
    return render(request, 'events/category_confirm_delete.html', {'category': category})

def participant_list(request):
    participants = Participant.objects.prefetch_related('events')
    return render(request, 'events/participant_list.html', {'participants': participants})

def participant_create(request):
    if request.method == 'POST':
        form = ParticipantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('participant_list')
    else:
        form = ParticipantForm()
    return render(request, 'events/participant_form.html', {'form': form, 'action': 'Create'})

def participant_update(request, pk):
    participant = get_object_or_404(Participant, pk=pk)
    if request.method == 'POST':
        form = ParticipantForm(request.POST, instance=participant)
        if form.is_valid():
            form.save()
            return redirect('participant_list')
    else:
        form = ParticipantForm(instance=participant)
    return render(request, 'events/participant_form.html', {'form': form, 'action': 'Update'})

def participant_delete(request, pk):
    participant = get_object_or_404(Participant, pk=pk)
    if request.method == 'POST':
        participant.delete()
        return redirect('participant_list')
    return render(request, 'events/participant_confirm_delete.html', {'participant': participant})
