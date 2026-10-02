#!/bin/bash
# Automated deployment script for Greenhill Co-op Ordering System

echo "Starting deployment..."

# Pull latest changes from main branch
git pull origin main

# Install Python dependencies
pip install -r requirements.txt

# Run all tests before deployment
pytest tests/

echo "Deployment complete."
