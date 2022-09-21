#!/usr/bin/python3

import os, django, sys

sys.path.append(".")

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "website.settings")
django.setup()


import officehours.models as models

aut22, created = models.Quarter.objects.get_or_create(ais_num = 2219,
                                                      year = 2022,
                                                      quarter = "aut")


cs141, created = models.Course.objects.get_or_create(ais_num = 56313,
                                                     subject = "CMSC",
                                                     catalog_code = 14100,
                                                     name = "Introduction to Computer Science I")

cs141_aut_22, created = models.CourseOffering.objects.get_or_create(course = cs141,
                                                                    quarter = aut22,
                                                                    url_slug = "cmsc14100-aut-22")
