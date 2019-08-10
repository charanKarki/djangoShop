$(document).ready(function () {
    $.get("/products/",
        function (data) {
            data.forEach(item => {
                $('#shopingItems').append(`
                <div class="col-lg-4 col-md-4 col-sm-6 mb-4">
            <div class="card h-100">
              <a href="#"><img class="card-img-top" src="http://placehold.it/700x400" alt=""></a>
              <div class="card-body">
                <h4 class="card-title">
                  <a href="{% url 'detail' %}" class="btn btn-success btn-md">${item.itemName}</a>
                </h4>
                <a href="#" class="btn btn-light btn-sm">Price $24.45</a>
                <a href="#" class="btn btn-light btn-sm dropdown-toggle"  id="triggerId" data-toggle="dropdown" aria-haspopup="true"
                aria-expanded="false">Size ${item.itemSize}</a>
                <div class="dropdown-menu" aria-labelledby="triggerId">
                <a class="dropdown-item" >6</a>
                <a class="dropdown-item ">7</a>               
                <a class="dropdown-item ">8</a>
                <a class="dropdown-item" >9</a>
               
                
            </div>
                <p class="card-text ">${item.discription}</p>
              </div>

              <div class="card-footer">
                <small class="text-muted">&#9733; &#9733; &#9733; &#9733; &#9734;</small>
              </div>
            </div>
          </div>
                `)
            });
        },
        "json"
    );
  })
