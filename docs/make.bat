@echo off
REM Build and clean documentation on Windows
if "%1" == "html" (
    sphinx-build -b html source build/html
    exit /b
)
if "%1" == "clean" (
    rmdir /s /q build
    exit /b
)
if "%1" == "help" (
    echo Usage: make [command]
    echo.
    echo Commands:
    echo   html     Build the HTML documentation
    echo   clean    Remove the built documentation
    echo   help     Show this help message
    exit /b
)
echo Invalid command. Use "make help" for a list of commands.
exit /b