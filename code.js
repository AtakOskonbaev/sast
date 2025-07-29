function() {
  query = search_field.value;
  $("#smart-search").empty();
  if (query.length > 2) {
    $.ajax({
      url: '/ru/search-api',
      data: 'query=' + query,
      method: 'get',
      success: function(data) {
        if (query.length > 2) {
          var html = ''
          for (let item of data.result) {
            if (!item.question) {
              let text = item.title.replace(RegExp(query, 'gi'), '&nbsp<strong>$&</strong>&nbsp')
              html = html + '<div class="item">\n' +
                '<a href="' + item.link + '"></a>\n' + text + '\n' +
                '</div>'
            } else {
              let text = item.question.replace(RegExp(query, 'gi'), '&nbsp<strong>$&</strong>&nbsp')
              html = html + '<div class="item">\n' +
                '<a href="' + item.link + '"></a>\n' + text + '\n' +
                '</div>'
            }
          }
          html = html.replace(RegExp(query, 'gi'), '&nbsp<strong>$&</strong>&nbsp')
          $("#smart-search").append(html)
        }
      },
      error: function(request, errorThrown, errorObject) {
        console.log(errorObject);
      }
    });
  }
}