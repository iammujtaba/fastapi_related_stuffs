# fastapi_related_stuffs
FastAPI interesting concepts.

FastAPI version :- 0.70
Python3 version :- 3.9.x

## Steps Test Django Like settings 
1. export FASTAPI_SETTINGS_MODULE (currently 3 modules are there)
    </br>
     a. main.development_settings
    </br>
     a. main.local_settings
     </br>
     a. main.production_settings
     </br>
     example: export FASTAPI_SETTINGS_MODULE=main.production_settings

2. Run python3 app.py 