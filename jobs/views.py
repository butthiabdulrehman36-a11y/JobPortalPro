from django.shortcuts import get_object_or_404, render

from .models import Job


def job_list(request):
    keyword = request.GET.get("q", "").strip()
    location = request.GET.get("location", "").strip()

    jobs = Job.objects.filter(is_active=True)

    if keyword:
        jobs = jobs.filter(
            title__icontains=keyword
        ) | jobs.filter(
            company_name__icontains=keyword
        ) | jobs.filter(
            description__icontains=keyword
        )

    if location:
        jobs = jobs.filter(
            location__icontains=location
        )

    return render(
        request,
        "jobs/job_list.html",
        {
            "jobs": jobs,
            "keyword": keyword,
            "location": location,
        },
    )


def job_detail(request, job_id):
    job = get_object_or_404(
        Job,
        id=job_id,
        is_active=True,
    )
    return render(
        request,
        "jobs/job_detail.html",
        {"job": job},
    )
