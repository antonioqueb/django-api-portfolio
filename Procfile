web: python manage.py collectstatic --no-input && gunicorn backend.wsgi --bind 0.0.0.0:$PORT --chdir /app --log-file - --workers 4 --timeout 120 --access-logfile - --error-logfile - --preload --max-requests 500 --max-requests-jitter 50  --log-level debug