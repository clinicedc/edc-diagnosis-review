#!/usr/bin/env python
import logging
import sys
from os.path import abspath, dirname, join

import django
from django.conf import settings
from django.test.runner import DiscoverRunner
from edc_test_utils import DefaultTestSettings

base_dir = dirname(abspath(__file__))
app_name = "edc_dx_review"

DEFAULT_SETTINGS = DefaultTestSettings(
    calling_file=__file__,
    BASE_DIR=base_dir,
    APP_NAME=app_name,
    ETC_DIR=join(base_dir, app_name, "tests", "etc"),
    EDC_DIAGNOSIS_REVIEW_APP_LABEL="edc_dx_review",
    SUBJECT_SCREENING_MODEL=f"edc_dx_review.subjectscreening",
    SUBJECT_CONSENT_MODEL=f"edc_dx_review.subjectconsent",
    SUBJECT_VISIT_MODEL=f"edc_dx_review.subjectvisit",
    SUBJECT_VISIT_MISSED_MODEL=f"edc_dx_review.subjectvisitmissed",
    SUBJECT_REQUISITION_MODEL=f"edc_dx_review.subjectrequisition",
    LIST_MODEL_APP_LABEL="edc_dx_review",
    INSTALLED_APPS=[
        "django.contrib.admin",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sessions",
        "django.contrib.messages",
        "django.contrib.staticfiles",
        "django.contrib.sites",
        "django_crypto_fields.apps.AppConfig",
        "django_revision.apps.AppConfig",
        "multisite",
        "edc_appointment.apps.AppConfig",
        "edc_action_item.apps.AppConfig",
        "edc_crf.apps.AppConfig",
        "edc_device.apps.AppConfig",
        # "edc_dashboard.apps.AppConfig",
        "edc_facility.apps.AppConfig",
        "edc_lab.apps.AppConfig",
        "edc_metadata.apps.AppConfig",
        "edc_offstudy.apps.AppConfig",
        "edc_reference.apps.AppConfig",
        "edc_registration.apps.AppConfig",
        "edc_identifier.apps.AppConfig",
        "edc_notification.apps.AppConfig",
        "edc_sites.apps.AppConfig",
        "edc_timepoint.apps.AppConfig",
        "edc_visit_schedule.apps.AppConfig",
        "edc_visit_tracking.apps.AppConfig",
        "edc_dx_review.apps.AppConfig",
    ],
    RANDOMIZATION_LIST_PATH=join(base_dir, app_name, "tests", "test_randomization_list.csv"),
    add_dashboard_middleware=True,
    use_test_urls=True,
).settings


def main():
    if not settings.configured:
        settings.configure(**DEFAULT_SETTINGS)
    django.setup()
    tags = [t.split("=")[1] for t in sys.argv if t.startswith("--tag")]
    failures = DiscoverRunner(failfast=False, tags=tags).run_tests([f"{app_name}.tests"])
    sys.exit(failures)


if __name__ == "__main__":
    logging.basicConfig()
    main()