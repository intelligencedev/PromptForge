# 🎨 PromptForge

A visual prompt management system for AI image generation. Organize, browse, and manage artistic style prompts with visual references in an intuitive interface.

![PromptForge Interface](https://img.shields.io/badge/Status-Active-success)
![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Flask](https://img.shields.io/badge/Flask-3.0-green)

## ✨ Features

- **Visual Catalog** - Browse hundreds of artistic styles with image previews and detailed descriptions
- **Organized Pages** - Group prompts into themed collections (Main Page, Camera, Materials, etc.)
- **Category Management** - Organize styles into customizable categories (Historical Art Movements, Traditional Media, Animation & Comics, 3D Rendering, etc.)
- **Interactive Cards** - Hover over images to view detailed prompt descriptions overlaid on the image
- **One-Click Copy** - Click any card to instantly copy the full prompt to clipboard
- **Search Across All Pages** - Quickly find specific styles across your entire library
- **Full CRUD Operations** - Add, edit, delete, and reorder prompts with an intuitive UI
- **JSON-Based Storage** - Each page stored as a separate JSON file for easy versioning and sharing
- **Dark Mode** - Toggle between light and dark themes for comfortable viewing
- **Import/Export** - Export individual pages as JSON for backup or sharing with others

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- A modern web browser

### Installation & Running

**Mac/Linux:**
```bash
./start.sh
```

**Windows:**
```
start.bat
```
or double-click the `start.bat` file

The script will automatically:
1. Check if Python is installed
2. Create a virtual environment (first run only)
3. Install dependencies (first run only)
4. Start the server

Then open your browser and go to: **http://localhost:5000**

### Manual Setup (Optional)

If you prefer to set up manually:

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On Mac/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the server
python app.py
```

## 📖 Usage

### Browsing Prompts
- Click on page buttons at the top to switch between different prompt collections
- Hover over any card to see the full description overlaid on the image
- Click a card to copy the prompt to your clipboard

### Managing Prompts
- **Add Page**: Click "Add Page" to create a new prompt collection
- **Add Category**: Click "Add Category" to create a new section within a page
- **Add Prompt**: Click "Add Prompt" within any category to add a new prompt card
- **Edit Prompt**: Click "Edit" on any card to modify the tag and description
- **Delete**: Remove individual prompts or entire categories
- **Reorder**: Use arrow buttons (← →) to change the order of prompts

### Searching
- Use the search bar to find prompts across all pages
- Results are grouped by page and category for easy navigation

### Exporting
- Click "Export JSON" at the bottom to download the current page as a JSON file
- Use "Save Page" to persist changes to the server

## 🗂️ Project Structure

```
img-prompt/
├── index.html          # Main application frontend
├── app.py             # Flask backend server
├── requirements.txt   # Python dependencies
├── start.sh          # Startup script (Mac/Linux)
├── start.bat         # Startup script (Windows)
├── Main Page.json    # Default prompts collection
├── CAMERA.json       # Camera-related prompts
├── MATERIALS.json    # Material-related prompts
└── images/           # Prompt preview images
```

## 🎯 Use Cases

Perfect for:
- **AI Artists** working with Midjourney, DALL-E, Stable Diffusion, or other AI art platforms
- **Designers** building a library of consistent style references
- **Creative Professionals** who need quick access to artistic terminology
- **Teams** sharing prompt libraries for consistent output

## 🛠️ Technical Stack

- **Frontend**: Vanilla JavaScript with Tailwind CSS
- **Backend**: Flask (Python) REST API
- **Storage**: JSON files (one per page)
- **Styling**: Tailwind CSS for responsive, modern design

## 📝 API Endpoints

- `GET /` - Serve the main application
- `GET /api/pages` - List all available JSON page files
- `GET /api/pages/<filename>` - Get specific page data
- `POST /api/pages` - Save/create a page
- `GET /images/<filename>` - Serve prompt preview images

## 🤝 Contributing

Feel free to fork this project and customize it for your needs. Some ideas:
- Add more artistic styles and categories
- Create specialized collections for specific AI tools
- Add image upload functionality
- Implement user authentication for multi-user environments

## 📄 License

This project is open source and available for personal and commercial use.

## 🐛 Troubleshooting

**Server won't start:**
- Make sure Python 3.8+ is installed: `python3 --version`
- Check if port 5000 is already in use
- Try running manually: `python app.py`

**Changes not saving:**
- Check browser console for errors
- Ensure the backend server is running
- Verify write permissions in the project directory

**Images not showing:**
- Ensure image files are in the `images/` directory
- Image names should match the prompt tag (with underscores for spaces)
- Supported formats: PNG, JPG

## 💡 Tips

- Use descriptive tags that match your image filenames
- Keep descriptions detailed but concise for better readability
- Organize prompts by workflow (e.g., styles, techniques, subjects)
- Regularly export your pages as backups
- Share JSON files with team members for consistent prompts

---

**Enjoy creating amazing AI art with PromptForge! 🎨✨**
