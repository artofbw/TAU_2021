#### Instalacja zależności

    pip install -r requirements.txt
    
    
#### Uruchomienie setuptools (generuje paczkę)

    Ekwiwalent Mavena dla pythona
    https://stackoverflow.com/questions/3324108/maven-equivalent-for-python
    
    tltr; setuptools

    python setup.py sdist
    

#### Uruchominie testów

    python setup.py test
    
    
    
#### CI

    https://github.com/artofbw/TAU_2021/pull/1 - failujący test
    
    Nie używałem Travisa za względu na strukturę repozytorium (nie można podpiąć pod konkrety katalog), zamiast tego użyłem github actions, konfiguracja w linku 
    https://github.com/artofbw/TAU_2021/blob/main/.github/workflows/ci.yml
