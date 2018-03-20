const booksData = require('../data/data.json');

self._organizeData = () => {
	const semesters = {};
	booksData.books_additional.forEach(d => {
		var semester = d["Semester"];
		if (!(semester in semesters)) {
			semesters[semester] = {
				numMale: 0,
				numFemale: 0,
			}
		}

		if (d["Gender"] == "male") {
			semesters[semester].numMale += 1;
		} else if (d["Gender"] == "female") {
			semesters[semester].numFemale += 1;
		}
	})

	const data = []
	for (var semester in semesters) {
		var proportion = semesters[semester].numFemale / 
			(semesters[semester].numFemale + semesters[semester].numMale)
		data.push({
			semester: semester,
			numMale: semesters[semester].numMale,
			numFemale: semesters[semester].numFemale,
			proportion: proportion,
		})
	}

	return data;
}

exports.drawGraph = (element) => {
	let data = _organizeData();

	const margin = {
	    top: 15,
	    right: 60,
	    bottom: 60,
	    left: 60,
	};

    const width = window.innerWidth * 0.5;
    const height = 300;

	const svg = d3.select(element).append("svg")
		.attr("class", "overall-time-graph")
	    .attr("width", width + margin.left + margin.right)
	    .attr("height", height + margin.top + margin.bottom)
	    .append("g")
	    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

	const domainSemesters = []
	for (let d in data) {
		domainSemesters.push(data[d].semester);
	}

	const x = d3.scale.ordinal()
	    .domain(domainSemesters)
	    .rangeBands([0, width]);

	const y = d3.scale.linear()
	    .domain([1, 0])
	    .range([0, height]);

	const valueline = d3.svg.line()
	    .x(function(d) { return x(d.semester); })
	    .y(function(d) { return y(d.proportion); });

	svg.append("path")	
		.attr("class", "line")
		.datum(data)
		.attr("d", valueline);

	svg.append("g")		
	.attr("class", "x-axis")
	.attr("transform", "translate(0," + height + ")")
	.call(d3.axisBottom(x))
	.selectAll("text")
		.attr("transform", "rotate(45)")
		.attr("y", 0)
	    .attr("x", 9)
	    .attr("dy", "1em")
		.style("text-anchor", "start");

	svg.append("g")		
		.attr("class", "y-axis")
		.call(d3.axisLeft(y));
};

