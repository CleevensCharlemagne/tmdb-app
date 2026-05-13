# TMDB CLI App

A simple Python command-line application that fetches movie data from the TMDB API.

🔗 **Project URL:** [https://roadmap.sh/projects/tmdb-cli](https://roadmap.sh/projects/tmdb-cli)
## Features

- Fetch popular movies
- Fetch top-rated movies
- Fetch upcoming movies
- Fetch currently playing movies
- Simple CLI interface using argparse
- Professional project structure
- Environment variable support for API keys

---

## Project Structure

```text
tmdb-app/
│
├── pyproject.toml
├── README.md
│
├── tmdb_app/
│   ├── __init__.py
│   ├── api.py
│   ├── cli.py
│   └── main.py
│
└── venv/
```

## Requirements
- Python 3.10+
- TMDB API Key

## Installation
### 1. Clone the repository
```bash
git clone <your-repository-url>
cd tmdb-app
```

### 2. Create a virtual environment
```bash
python -m venv venv
```

### 3. Activate the virtual environment
#### Windows: powrshell
```powershell
venv\Scripts\activate
```

#### Linux / macOS
```bash
source venv/bin/activate
```

### 4. Install the project
```bash
pip install -e .
```

## Configure the API Key

You must create a TMDB API key from:

- https://www.themoviedb.org/settings/api

Then set the environment variable.

### Windows PowerShell

```powershell
setx TMDB_API_KEY "your_api_key"
```

Restart your terminal after setting the variable.

### Linux / macOS

```bash
export TMDB_API_KEY="your_api_key"
```

## Usage

### Fetch popular movies

```bash
tmdb-app --type 'popular'
```

### Fetch top-rated movies

```bash
tmdb-app --type 'top'
```

### Fetch upcoming movies

```bash
tmdb-app --type 'upcoming'
```

### Fetch currently playing movies

```bash
tmdb-app --type 'playing'
```

## Example Output

```text
Fight Club:
    adult: False
    backdrop_path: /path.jpg
    genre_ids: [18]
    id: 550
    original_language: en
    original_title: Fight Club
------------------------------------------------------------
```

## Technologies Used

- Python
- Requests
- Argparse
- TMDB API

---

## Future Improvements

- Better terminal formatting
- Colored output
- Pagination support
- Search movies by name
- TV show support
- Multiple commands using subparsers
- Rich terminal UI

---

## License

This project is licensed under the MIT License.

---

## Author

Developed as a learning project to practice:

- API integration
- CLI application development
- Python project structure
- Packaging Python applications
