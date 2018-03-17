const booksData = require('../data/data.json');

exports.drawProfessorsGivenSemester = function(element, sem) {
	/*
		professors = {
			<professorName>: {
				<semester>: {
					males: int,
					females: int,
				}, 
				...	
			}, 
			...
		}
	*/
	var professors = {} 

	booksData.books_additional.forEach(d => {
	  var professor = d["Professor"];
	  var semester = d["Semester"];

	  if (!(professor in professors)) {
	  	professors[professor] = {};
	  } 

	  var currentProfessor = professors[professor]
	  if (!(semester in currentProfessor)) {
	  	currentProfessor[semester] = {
	  		males: 0,
	  		females: 0,
	  	}
	  }

	  if (d["Gender"] == "male") {
	  	// max for those whose num students is not recorded
	  	currentProfessor[semester].males += 1;
	  } else if (d["Gender"] == "female") {
	  	currentProfessor[semester].females += 1;
	  }
	})

	var profData = []
	for (var p in professors) {
		if (p == "Noinstructor") {
			continue;
		}
		var prof = professors[p]
		profData.push({
			name: p,
			semesterData: prof, // mapping of semester to num male/female
		});
	}


	var data = profData.filter(d => d.semesterData[sem]);
	data = data.sort(function(a, b) {

		var aTotalMale = 0;
		var aTotalFemale = 0;
		for (var semester in a.semesterData) {
			aTotalMale += a.semesterData[semester].males;
			aTotalFemale += a.semesterData[semester].females;
		}

		var bTotalMale = 0;
		var bTotalFemale = 0;
		for (var semester in b.semesterData) {
			bTotalMale += b.semesterData[semester].males;
			bTotalFemale += b.semesterData[semester].females;
		}

		return (aTotalFemale / (aTotalMale + aTotalFemale) - 
				bTotalFemale / (bTotalMale + bTotalFemale));
	});

	// // only top and bottom five
	// var bottomFive = data.slice(0, 6);
	// var topFive = data.slice(data.length - 6, data.length);
	// var data = topFive.concat(bottomFive);

	var margin = {
	    top: 15,
	    right: 25,
	    bottom: 15,
	    left: 200,
	};

    var width = window.innerWidth * 0.5;
    var height = 500;

	var svg = d3.select(element).append("svg")
	    .attr("width", width + margin.left + margin.right)
	    .attr("height", height + margin.top + margin.bottom)
	    .append("g")
	    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

	var x = d3.scale.linear()
	    .range([0, width])
	    .domain([0, 1]);

	var y = d3.scale.ordinal()
	    .rangeRoundBands([height, 0], .1)
	    .domain(data.map(function (d) {
	        return d.name;
	    }));

	//make y axis to show bar names
	var yAxis = d3.svg.axis()
	    .scale(y)
	    //no tick marks
	    .tickSize(0)
	    .orient("left");

	var gy = svg.append("g")
	    .attr("class", "y axis")
	    .call(yAxis)

	var bars = svg.selectAll(".bar")
	    .data(data)
	    .enter()
	    .append("g")

	// append rects - female
	bars.append("rect")
	    .attr("class", "bar")
	    .attr("y", function (d) {
	        return y(d.name);
	    })
	    .attr("height", y.rangeBand())
	    .attr("x", 0)
	    .attr("width", function (d) {
	    	if (d.semesterData[sem].males + d.semesterData[sem].females == 0) {
	    		return x(0);
	    	}
	        return x(d.semesterData[sem].females / (d.semesterData[sem].males + d.semesterData[sem].females));
	    })
	    .attr("fill", "#ff99cc");

	// append rects - male
	bars.append("rect")
	    .attr("class", "bar")
	    .attr("y", function (d) {
	        return y(d.name);
	    })
	    .attr("height", y.rangeBand())
	    .attr("x", function(d) {
	    	if (d.semesterData[sem].males + d.semesterData[sem].females == 0) {
	    		return x(0);
	    	}
	    	
	        return x(d.semesterData[sem].females / (d.semesterData[sem].males + d.semesterData[sem].females));
	    })
	    .attr("width", function (d) {
	    	if (d.males + d.females == 0) {
	    		return x(0);
	    	}
	        return x(1 - d.semesterData[sem].females / (d.semesterData[sem].males + d.semesterData[sem].females));
	    })
	    .attr("fill", "#99ccff");

	// append text
	bars.append("text")
	    .attr("class", "label")
	    // y position of the label is halfway down the bar
	    .attr("y", function (d) {
	        return y(d.name) + y.rangeBand() / 2 + 4;
	    })
	    .attr("x", function (d) {
	        return x(0.5);
	    })
	    .text(function (d) {
	        return d.semesterData[sem].females + ", " + d.semesterData[sem].males;
	    });

}