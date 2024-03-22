document.addEventListener('DOMContentLoaded', function () {
    // По умолчанию показываем контейнер "order"
    document.getElementById('order').style.display = 'block';
    document.getElementById('addres').style.display = 'none';

    // Обработчики событий для пунктов меню
    document.getElementById('dashboard').addEventListener('click', function () {
        document.getElementById('order').style.display = 'block';
        document.getElementById('addres').style.display = 'none';
    });

    document.getElementById('addresses').addEventListener('click', function () {
        document.getElementById('order').style.display = 'none';
        document.getElementById('addres').style.display = 'block';
    });

    // Добавьте обработчики для других пунктов меню при необходимости
});


function showAddressForm() {
    document.getElementById("newAddressForm").style.display = "block";
    document.getElementById("editForm").style.display = "none";
}

function showEditForm() {
    document.getElementById("editForm").style.display = "block";
    document.getElementById("newAddressForm").style.display = "none";
}

function deleteAddress() { //надо исправить 
    $.ajax({
        type: 'DELETE',
        url: '{% url "user:delete_address" %}', // Замените на фактический URL вашего обработчика удаления адреса
        data: {
            csrfmiddlewaretoken: '{{ csrf_token }}'
        },
        success: function(response) {
            alert("Адрес успешно удален!");
            $('.account__details.two').hide(); // Скрываем блок с адресом
        },
        error: function(response) {
            alert('Произошла ошибка при удалении адреса. Пожалуйста, попробуйте позже.');
        }
    });
}