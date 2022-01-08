@echo off

SET mypath=%~dp0
SET p1=%mypath:~0,-1%\ss2qr.py

python %p1% %1