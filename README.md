# Diplom_3
 третья часть дипломной работы
 было много коммитов и решил слить всё в запасную ветку, потом переименовал её в develop3
 старую удалил, выполнял командами

 $ git checkout --orphan temp_branch
 $ git branch -D develop3 , потом 
 $ git push origin develop3 --force

  документация по API - https://code.s3.yandex.net/qa-automation-engineer/python-full/diploma
  /api-documentation.pdf?etag=3403196b527ca03259bfd0cb41163a89
  папка source содержит внутри себя папки с файлами, опысающими страницы веб-приложения
  

 test_follow_to_constructor_page проверяет переход по клику на «Конструктор»
 test_follow_to_orders_feed_page проверяет переход по клику на «Лента заказов»
 test_check_fluorescent_bun_form проверяет, что если кликнуть на ингредиент, появится всплывающее окно с деталями
 test_close_fluorescent_bun_form проверяет, что всплывающее окно закрывается кликом по крестику
 test_counter_ingredient проверяет, что при добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента
 test_create_order проверяет, что залогиненный пользователь может оформить заказ
 test_follow_to_personal_page проверяет переход по клику на «Личный кабинет»
 test_follow_to_feed_orders проверяет переход в раздел «История заказов»
 test_exit_personal_page проверяет выход из аккаунта
 test_follow_to_the_password_recovery_page проверяет переход на страницу восстановления пароля по кнопке «Восстановить пароль»
 test_input_password_and_click_recovery_button проверяет ввод почты и клик по кнопке «Восстановить»
 test_checking_the_show_of_the_password_field проверяет клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его
 test_check_order_info_window проверяет, что если кликнуть на заказ, откроется всплывающее окно с деталями
 test_check_user_orders_in_orders_history, что заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»
 test_update_counter_orders, что при создании нового заказа счетчик Выполнено за всё время / Выполнено за сегодня увеличивается
 test_check_user_order_in_job проверяет, что после оформления заказа его номер появляется в разделе В работе

Установка зависимостей

$ pip install -r requirements.txt

Запуск автотестов и создание HTML-отчета о покрытии

$ pytest --alluredir=./allure_results tests/
$ pytest --cov=praktikum --cov-report=html`

Яндекс Практикум 2025 , Москва , планета Земля
