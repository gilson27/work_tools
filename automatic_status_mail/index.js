/**
 * @fileoverview 
 * @author <gilsonvarghese7@gmail.com>
 * @date 22nd June 2017 
*/

var csvReader = require("csv_reader/csv_reader");
var mailClient = require("mail/send_mail");

/**
 * Send Status Mail every morning
*/
var sendStatus = function() {
	readCSV();
	checkStatus();
	sendMail();
	updateStatus();
};

/**
 * Start of program to send status
*/
sendStatus();
