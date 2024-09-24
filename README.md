# Online Shop



## Содержание

- [Установка](#установка)
- [Использование](#использование)
- [Задачи](#задачи)
- [Лицензия](#лицензия)
- [Обновления](#обновления)

## Установка

--

## Задачи

- [x] Первичтная реализация моделей `Product`,`Orders`,`Users`
- [x] Настройка связей между моделями
- [x] `Product` несколько изображений
- [ ] Реализация регистрации `Users`
- [ ] Реализация заказов `Orders`
- [x] Реализация отображения `Product` на основной странице
- [ ] Реализация отображения отдельного `Product`
- [ ] Функционал похожие `Product`
- [ ] Добавление поиска для `Product`
- [ ] Добавление фильтров для `Product`
- [ ] Рейтинг (Доп функционал `Product`)
- [ ] Отзывы (Доп функционал `Product`)
- [ ] Бренд (Доп функционал `Product`)
- [x] Тип (Доп функционал `Product`)
- [ ] Отображение статусов New, Скидка, Акция (Доп функционал `Product`)
- [ ] Реализация избранных `Product`
- [ ] Выбор страны/города магазина


## Обновления

### [0.1.0] - 2023-09-21
- Создан базовый проект с установкой Django.
- Добавлены модели: `Product`,`Orders`,`Users`
- Начальная реализация модели `Product`.

### [0.1.1] - 2023-09-22
- Установил интерфейс Unfold.
- Начальная реализация моделей `Orders`, `Users`.
> [!IMPORTANT]
> У orders нужно присваивать статус по умолчанию
- Настройка связей между моделями.

### [0.1.2] - 2023-09-23
- Обновил модели:
* `Product` имеет возможность загрузки нескольких изображений с выбором основного для отображения на фронте
* Добавлен `Product type`
- Начальная реализация фронта
- Добавлено горизонтальное меню с фиксацией при скроллинге
- Добавлено отображение `Product`
> [!IMPORTANT]
> Перенос иконок лк, карзины и поиска при скроллинге

### [0.1.3] - 2023-09-24
- Начальная реализация личного кабинет
> [!IMPORTANT]
> Доделать стили полей
- Pop-up логин
- Страница регистрации
- Страница профиля
