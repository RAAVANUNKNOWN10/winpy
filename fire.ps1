#Start-Process "C:\Program Files\Mozilla Firefox\firefox.exe"


Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.SecurityProtocolType]::Tls12; Invoke-Expression ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))


# Check if Chocolatey is installed, and if not, install it
if (-not (Get-Command choco -ErrorAction SilentlyContinue)) {
    Set-ExecutionPolicy Bypass -Scope Process -Force;
    [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.SecurityProtocolType]::Tls12; Invoke-Expression ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
}

# List of common development tools for PyQt and Python projects
$packages = @(
    "python"            # Install Python (latest version)
    #"git",                # Install Git (if you need version control)
    #"visualstudiocode",   # Install Visual Studio Code (as an IDE)
    #"notepadplusplus",    # Install Notepad++ (optional, for quick text editing)
    #"7zip"                # Install 7-Zip (optional, for file compression)
)

# Install required development tools
foreach ($package in $packages) {
    choco install $package -y
}

# Install Python dependencies for PyQt
Write-Host "Installing Python dependencies..."

# Install pip (Python's package installer) if not already installed
python -m ensurepip --upgrade

# Upgrade pip to the latest version
python -m pip install --upgrade pip

# Install PyQt5 and related packages for GUI development
pip install pyqt6

# Optionally, install PyQtWebEngine for web-based components
pip install pyqtwebengine

# Install other commonly used libraries for PyQt apps
pip install numpy  # For numerical computations (optional, depends on your app)
pip install matplotlib  # For plotting and visualizations (optional)
pip install sqlalchemy  # For database support (optional)

# Output completion message
Write-Host "PyQt environment set up successfully!"

