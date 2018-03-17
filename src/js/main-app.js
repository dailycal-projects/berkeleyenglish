require('../scss/main.scss');
// const d3 = require('d3');
const booksData = require('../data/data.json');
const professors = require('./professors.js');

window.$('.icon-facebook').click((e) => {
  e.preventDefault();
  const uri = encodeURIComponent(window.location.href);
  window.open(`https://www.facebook.com/sharer/sharer.php?u=${uri}`);
});


window.$('.icon-twitter').click((e) => {
  e.preventDefault();
  const uri = window.location.href;
  const status = encodeURIComponent(`${window.tweetText} ${uri}`);
  window.open(`https://twitter.com/home?status=${status}`);
});

// https://gist.github.com/mathewbyrne/1280286
function slugify(text)
{
  return text.toString().toLowerCase()
    .replace(/\s+/g, '-')           // Replace spaces with -
    .replace(/[^\w\-]+/g, '')       // Remove all non-word chars
    .replace(/\-\-+/g, '-')         // Replace multiple - with single -
    .replace(/^-+/, '')             // Trim - from start of text
    .replace(/-+$/, '');            // Trim - from end of text
}

professors.drawProfessorsGivenSemester("#everything", "Fall 2017");

$("#button").click(function() {
  $(".bar").filter(function(_, element) { return $(element).attr('x') == "0";})
           .attr("display", "none");
});
// dropDown.on("change", function () {
//     var selected = this.value;

//     hGsvg.selectAll(".bar")
//         .filter(function(d) {return (selected !== d[0]); })
//         .attr("display", 'none');

//     hGsvg.selectAll(".bar")
//         .filter(function(d) {return (selected === d[0]); })
//         .attr("display", 'inline')
//         .each(function(d) { helpers.mouseover(d) });
// });
