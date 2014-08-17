#skrypt logowania do domeny
echo Ustawiam aktualny czas
net time \\SALA37 /set /yes
echo Mapuje stacje sieciowe na udzia³y serwera SALA33
net use x: \\debian\homes
net use z: \\debian\informatyka
