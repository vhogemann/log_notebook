# LogNotebook VS Code Setup

This guide explains how to set up Visual Studio Code to run the LogToGraph.ipynb Jupyter notebook directly in the editor.

## Prerequisites

1. **Visual Studio Code** - Download from [code.visualstudio.com](https://code.visualstudio.com/)
2. **Python 3.8+** - Download from [python.org](https://python.org/downloads/)
3. **Your Humio token**

## Setup Instructions

### 1. Install Required VS Code Extensions

Install these essential extensions in VS Code:

- **Python** (ms-python.python) - Python language support
- **Jupyter** (ms-toolsai.jupyter) - Jupyter notebook support
- **Python Debugger** (ms-python.debugpy) - Debugging support

You can install them via:
- **Command Palette**: `Cmd+Shift+P` → "Extensions: Install Extensions"
- **Extensions View**: Click the Extensions icon in the sidebar
- **Command Line**: 
  ```bash
  code --install-extension ms-python.python
  code --install-extension ms-toolsai.jupyter
  code --install-extension ms-python.debugpy
  ```

### 2. Environment Variables

Copy the example environment file and add your Humio token:

```bash
cp example.env .env
```

Edit `.env` and replace `your_humio_token_here` with your actual Humio token:

```
HUMIO_TOKEN=your_actual_humio_token_here
```

### 3. Python Environment Setup

#### Option A: Virtual Environment (Recommended)

Create and activate a virtual environment:

```bash
# Create virtual environment
python3 -m venv lognotebook-env

# Activate it (macOS/Linux)
source lognotebook-env/bin/activate

# Install dependencies
pip install -r requirements.txt
```

#### Option B: Conda Environment

```bash
# Create conda environment
conda create -n lognotebook python=3.9

# Activate it
conda activate lognotebook

# Install dependencies
pip install -r requirements.txt
```

### 4. Configure VS Code Python Interpreter

1. **Open the project** in VS Code:
   ```bash
   code .
   ```

2. **Select Python Interpreter**:
   - Press `Cmd+Shift+P` 
   - Type "Python: Select Interpreter"
   - Choose your virtual environment interpreter:
     - For venv: `./lognotebook-env/bin/python`
     - For conda: Select the conda environment

3. **Verify Setup**:
   - Open `LogToGraph.ipynb`
   - VS Code should automatically detect it as a Jupyter notebook
   - Click "Select Kernel" in the top-right and choose your Python environment

## Running the Notebook

### 1. Open the Notebook

- Open `LogToGraph.ipynb` in VS Code
- The file will automatically open in Jupyter notebook mode

### 2. Environment Variables

VS Code will automatically load environment variables from your `.env` file when running Python code.

### 3. Install System Dependencies

For Graphviz support (required for flowchart generation):

**macOS:**
```bash
brew install graphviz
```

**Ubuntu/Debian:**
```bash
sudo apt-get install graphviz graphviz-dev
```

### 4. Run Cells

- **Run single cell**: Click the ▶️ play button next to a cell or press `Shift+Enter`
- **Run all cells**: Use Command Palette → "Jupyter: Run All Cells"
- **Run cells above**: Command Palette → "Jupyter: Run All Cells Above"

## Features in VS Code

### ✅ **Rich Notebook Experience**
- Syntax highlighting and IntelliSense
- Interactive outputs and visualizations
- Built-in variable explorer
- Integrated debugging

### ✅ **Development Tools**
- Git integration
- Terminal integration
- Code formatting and linting
- Autocomplete and error detection

### ✅ **Debugging Support**
- Set breakpoints in notebook cells
- Step through code execution
- Inspect variables and call stack

### ✅ **Extensions Ecosystem**
- GitLens for Git integration
- Python Docstring Generator
- Jupyter Slide Show
- Live Share for collaboration

## Troubleshooting

### 1. **Kernel Issues**

If the kernel won't start:
- Check that your Python environment is properly activated
- Verify all dependencies are installed: `pip list`
- Restart VS Code and try again
- Use Command Palette → "Jupyter: Restart Kernel"

### 2. **Import Errors**

If you get import errors:
- Make sure you've selected the correct Python interpreter
- Verify the virtual environment is activated
- Install missing packages: `pip install <package_name>`

### 3. **Environment Variables Not Loading**

If your Humio token isn't working:
- Ensure `.env` file exists in the project root
- Check the file contains: `HUMIO_TOKEN=your_actual_token`
- Restart the kernel after creating/modifying `.env`

### 4. **Graphviz Errors**

If flowchart generation fails:
- Install Graphviz system package (see installation commands above)
- Restart VS Code after installing Graphviz
- Verify installation: `dot -V` in terminal

### 5. **Output Directory Permissions**

If you can't save files to the output directory:
```bash
mkdir -p output
chmod 755 output
```

## VS Code Settings

You can add these settings to your VS Code workspace for a better experience:

Create `.vscode/settings.json`:

```json
{
    "python.defaultInterpreterPath": "./lognotebook-env/bin/python",
    "jupyter.askForKernelRestart": false,
    "jupyter.interactiveWindow.collapseCellInputCodeByDefault": false,
    "python.terminal.activateEnvironment": true,
    "files.associations": {
        "*.ipynb": "jupyter-notebook"
    }
}
```

## Useful VS Code Shortcuts

- **Run Cell**: `Shift+Enter`
- **Run Cell and Insert Below**: `Alt+Enter`
- **Command Palette**: `Cmd+Shift+P`
- **Quick Open**: `Cmd+P`
- **Toggle Terminal**: `Ctrl+`` ` 
- **Split Editor**: `Cmd+\`

## Next Steps

Once everything is set up:

1. Open `LogToGraph.ipynb` in VS Code
2. Update the `correlation_id`, `repo`, and `start` parameters in cell 2
3. Run all cells to generate your log analysis and flowcharts
4. View the generated SVG files in the `output/` directory

Your VS Code environment is now ready for interactive log analysis and visualization!
