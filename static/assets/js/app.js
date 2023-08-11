$(document).ready(function () {
    $('#qty').val(0);
    $('#add').on('click', function () {
        let qty = parseInt($('#qty').val()) + 1
        $('#qty').val(qty);
    })
    $('#reduce').on('click', function () {
        let qty = parseInt($('#qty').val()) - 1
        if (qty >= 0) {
            $('#qty').val(qty);
        }
    })
    $('.size-selection').on('click', function (e) {
        size = $(this).data('val')
    })
    $('.color-selection').on('click', function (e) {
        color = $(this).data('val')
    })
    $('#add-cart').on('click', function (e) {
        qty = $('#qty').val()
        if (!size) {
            alert('Please select a size')
            return
        }
        if (!color) {
            alert('Please select a color')
            return
        }
        if (qty == 0) {
            alert('Please select a Quantity')
            return
        }
        id = $('#id').val()
        $.ajax({
            type: 'GET',
            url: `/api/add-cart/${id}`,
            data: {
                qty, size, color
            },
            success: function (data) {
                alert(data.message)
                $('#cart-head').load(document.URL + ' #cart-head');

            }
        })
    })
    $('.add-cart').on('click', function (e) {
        id = $(this).data('val')
        $.ajax({
            type: 'GET',
            url: `/api/add-cart-common/${id}`,
            success: function (data) {
                alert(data.message)
                $('#cart-head').load(document.URL + ' #cart-head');

            }
        })
    })
    $('.add-wishlist').on('click', function (e) {
        id = $(this).data('val')
        $.ajax({
            type: 'GET',
            url: `/api/add-wishlist/${id}`,
            success: function (data) {
                alert(data.message)
                $('#wish-head').load(document.URL + ' #wish-head');

            }
        })
    })
    $('.rm-cart').on('click', function (e) {
        id = $(this).data('val')
        if (confirm('Are you sure you want to delete this cart item?'))
            $.ajax({
                type: 'GET',
                url: `/api/rm-cart/${id}`,
                success: function (data) {
                    $('#cart-head').load(document.URL + ' #cart-head');
                    $('#cart-list').load(document.URL + ' #cart-list');
                }
            })
    })
    $('.rm-wishlist').on('click', function (e) {
        id = $(this).data('val')
        if (confirm('Are you sure you want to delete this wish?'))
            $.ajax({
                type: 'GET',
                url: `/api/rm-wish/${id}`,
                success: function (data) {
                    $('#wish-head').load(document.URL + ' #wish-head');
                    $('#wish-list').load(document.URL + ' #wish-list');

                }
            })
    })
    function toggle(int) {
        if (int) {
            int = 0;
        } else {
            int = 1;
        }
        return int
    }
    function makeFilter(param, array) {
        if (!$(param).data('checked')) {
            array.push($(param).data('value'))
        }
        else {
            array.pop($(param).data('value'))
        }
        $(param).data('checked', toggle($(param).data('checked')))
    }
    
    let category_array = [];
    let brand_array = [];
    $('.category-filter').on('change', function () {
        makeFilter(this, category_array)
    });

    $('.brand-filter').on('change', function () {
        makeFilter(this, brand_array)
    });
})
