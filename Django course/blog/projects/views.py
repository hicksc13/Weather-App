from django.shortcuts import render
from django.http import HttpResponse


def projects(rquest):
    return HttpResponse('MANY projects')

def project(rquest):
    return HttpResponse('SINGLE Project')

