let filter = function () {
    document.getElementById('list').hidden = true;
    
    input.addEventListener('keyup', function () {
        let filter = input.value.toLowerCase(),
            filterItems = document.querySelectorAll('#list li');

        filterItems.forEach(item => 
            {
            if (item.innerHTML.toLowerCase().indexOf(filter) > -1) 
            {
                item.style.display = '';
                document.getElementById('list').hidden = false;
            } 
            else 
            {
                item.style.display = 'none';
            }
            document.getElementById('input').onclick = function() 
            {
                document.getElementById('list').hidden = true;
            }
        })
    })
};
filter();