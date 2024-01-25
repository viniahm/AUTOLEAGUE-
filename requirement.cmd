@echo off
echo Baixando a biblioteca lcu_driver...
pip install lcu-driver
if %errorlevel% equ 0 (
    echo Instalação concluída com sucesso.
) else (
    echo Houve um problema durante a instalação.
)
pause
