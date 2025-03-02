 
from django.shortcuts import render, redirect, get_object_or_404
from .models import School, Classroom
from .forms import SchoolForm, ClassroomForm

 
def school_list(request):
    schools = School.objects.all()
    return render(request, 'school/school_list.html', {'schools': schools})

 
def school_create(request):
    if request.method == 'POST':
        form = SchoolForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('school_list')
    else:
        form = SchoolForm()
    return render(request, 'school/school_form.html', {'form': form})

 
def school_update(request, pk):
    school = get_object_or_404(School, pk=pk)
    if request.method == 'POST':
        form = SchoolForm(request.POST, instance=school)
        if form.is_valid():
            form.save()
            return redirect('school_list')
    else:
        form = SchoolForm(instance=school)
    return render(request, 'school/school_form.html', {'form': form})

 
def school_delete(request, pk):
    school = get_object_or_404(School, pk=pk)
    if request.method == 'POST':
        school.delete()
        return redirect('school_list')
    return render(request, 'school/school_confirm_delete.html', {'school': school})

 
def classroom_list(request):
    classrooms = Classroom.objects.all()
    return render(request, 'school/classroom_list.html', {'classrooms': classrooms})

 
def classroom_create(request):
    if request.method == 'POST':
        form = ClassroomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('classroom_list')
    else:
        form = ClassroomForm()
    return render(request, 'school/classroom_form.html', {'form': form})
