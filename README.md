# GSheetSync

GSheetSync is a Python tool for seamlessly synchronizing and updating data in Google Sheets.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [Folder Structure](#folder-structure)
- [Contributing](#contributing)
- [Getting Google Credentials](#getting-google-credentials)

## Prerequisites

- **Docker**: Install [Docker](https://docs.docker.com/get-docker/).
- **Docker Compose**: Install [Docker Compose](https://docs.docker.com/compose/install/).
- **Google Service Account**: Set up a Google Service Account and download the credentials JSON file.

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/ASonneP/GSheetSync.git
cd GSheetSync
```

### 2. Setup the Environment Variables

Create a `.env` file by copying the `.env.template`:

```bash
cp .env.template .env
```

Fill in the necessary values in the `.env` file:

```dotenv
CREDS_JSON=path_to_your_service_account.json
USER_NAME=your_username
MESSAGE="Your custom message"
```

### 3. Build and Run with Docker Compose

To build and run the project with Docker Compose, use the following command:

```bash
docker-compose up --build
```

This will build the Docker image, start the container, and run the GSheetSync script.

### 4. Run in Detached Mode (Optional)

If you want to run the container in the background, use:

```bash
docker-compose up -d
```

### 5. Stopping the Service

To stop the running containers, use:

```bash
docker-compose down
```

## Folder Structure

```plaintext
├── .env.template        # Environment variable template
├── Dockerfile           # Dockerfile to build the Docker image
├── docker-compose.yml   # Docker Compose configuration
├── gsheet-432108-e1f33c6a12f3.json  # Service account JSON (add to .gitignore)
├── requirements.txt     # Python dependencies
├── update_ip.py         # Main script to update Google Sheets
└── README.md            # Project documentation
```

## Contributing

If you'd like to contribute to GSheetSync, please fork the repository and use a feature branch. Pull requests are warmly welcome.

## Getting Google Credentials

To use GSheetSync, you'll need to create a Google Service Account and get the credentials JSON file. Here's how:

### 1. Go to the Google Cloud Console: Visit [Google Cloud Console](https://console.cloud.google.com/).

### 2. Create a New Project: If you don't already have a project, create a new one.

### 3. Enable Google Sheets API:

- Navigate to "APIs & Services" > "Library."

- Search for "Google Sheets API" and click "Enable."

### 4. Create a Service Account:

- Go to "APIs & Services" > "Credentials."

- Click "Create Credentials" > "Service Account."

- Fill in the required details and create the service account.

### 5. Download the Credentials JSON:

- After creating the service account, go to the "Keys" section.

- Click "Add Key" > "Create New Key" and choose JSON.

- Download the JSON file and save it securely; this file will be used as CREDS_JSON in the .env file.

### 6. Share the Google Sheet with the Service Account:

- Open your Google Sheet.
- Share it with the email address listed in your JSON credentials file (found under client_email).
