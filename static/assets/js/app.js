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
    $('.get-product').on('click', function (e) {
        id = $(this).data('val')
        $.ajax({
            type: 'GET',
            url: `/api/get-product/${id}`,
            success: function (data) {
                console.log(data.data.name);
                console.log(data.data.price);
                console.log(data.data.sizes);
                console.log(data.data.sizes_ids);
                console.log(data.data.colors);
                console.log(data.data.colors_ids);
                console.log(data.data.available_quantity);
                console.log(data.data.discounted_price);
                console.log(data.data.total_price);
                let color_ids = data.data.colors_ids
                let sizes_ids = data.data.sizes_ids
                let sizes = data.data.sizes
                let colors = data.data.colors
                let color_comp = ''
                let size_comp = ''
                sizes_ids?.map(index, element =>{
                   color_comp += `<div class="size-selector">
                                    <input type="radio" name="size" id="size-{{product_has_size.size.id}}" class="hidden">
                                    <label for="size-{{product_has_size.size.id}}" data-val="{{product_has_size.size.id}}"
                                        class="text-xs border border-gray-200 size-selection rounded-sm h-6 w-6 flex items-center justify-center cursor-pointer shadow-sm text-gray-600">{{product_has_size.size.display_name}}</label>
                                </div>`
                })
                $('#color-list').append(color_comp)
                sizes_ids?.map(index, element =>{
                    size_comp += `<div class="color-selector">
                                    <input type="radio" name="color" id="{{product_has_color.id}}-{{product_has_color.color.hex}}"
                                        class="hidden">
                                    <label for="{{product_has_color.id}}-{{product_has_color.color.hex}}"
                                        data-val="${element}"
                                        class="border border-gray-200 rounded-sm h-6 w-6  cursor-pointer shadow-sm block color-selection"
                                        style="background-color: #{{product_has_color.color.hex}};"></label>
                                    </div>`
                })
                $('#size-list').append(size_comp)
               
                

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

    $('.update-cart-item').on('click', function () {
        alert('something')
        console.log($(this).data('sizes'))
        $(this).data('sizes').map(ele => console.log(ele))
    });

})
