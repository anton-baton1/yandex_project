# SAPW<br>
## Жанр: 2D-Платформер<br>

#### Это одиночноя игра, в которой Вы играете за паука, которому нужно находить выход из уровня, вы можете цепляться паутиной за разные выступы и платформы, но будьте экономнее, паутина не бесконечна...
#
+ #### В каждом уровне персонаж появляется в одном и том же месте<br>
+ #### Проходя уровни вы можете увеличивать кол-во паутины и её длину<br>
+ #### Управление персонажем происходит мышью и клаватурой<br>
+ #### В некоторых уровнях вам могут попасться злые насекомые, так что будьте осторожнее<br>

## ТЗ
+ Реализовать класс паука
+ Реализовать класс платформ
+ Реализовать класс паутины
+ Реализовать перемещение паука на клавиши
+ Создать уровни
+ Сделать карту уровней
+ Сделать главное окно
  + Сделать кнопку начала игры
  + Сделать кнопку настроек
+ Сделать окно, показавающееся, после прохождения уровня
+ Сделать окно, показавающееся, после поражения

## Пояснительная записка
**Название**: SAPW<br>
**Автор**: Лодыгин Антон<br>
**Идея**: Создать игру, в которой пользователь будет играть за паука, проходя разные уровни<br>
**Реализация**:<br>&emsp;
В файле generate_level реализованна функия generate_level для создания уровня.Уровни берутся из папки maps.<br>&emsp;
Все картинки лежат в папке data<br>&emsp;
В файле spider.py реализован класс Spider паука.<br>&emsp;
В файле platform.py реализован класс Platform платформ.<br>&emsp;
В файле web.py реализован класс Web паутины.<br>&emsp;
В файле timer.py реализован класс Timer таймера.<br>&emsp;
В файле start_screen.py реализованна функция start_screen главного окна.<br>&emsp;
В файле terminate.py реализованна функция terminate корректного закрытия игры.

**Используемые библиотеки**:
+ *sys* для корректного выхода из игры
+ *pygame* для реализации игры
+ *math* для математических вычислений

**Презентация** - https://docs.google.com/presentation/d/1zkGR5NcRLqAxq2EeSL5cnBq5IKEPp-YD_DGanIFpIsg/edit?usp=sharing

