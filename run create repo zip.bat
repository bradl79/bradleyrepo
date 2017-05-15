@echo off
if exist "*.zip" (del *.zip)
7z a -tzip -r repository.bradley.zip %cd%/~repo/* 