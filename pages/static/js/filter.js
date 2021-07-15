$(".filter-manager").change(function () {
  filter_manager_function();
});

$("table tbody tr").show(); //intially all rows will be shown

function filter_manager_function() {
  $("table tbody tr").hide(); //hide all rows

  var positionFlag = 0;
  var positionValue = $("#position_filter").val();
  var homelandFlag = 0;
  var homelandValue = $("#homeland_filter").val();

  //setting intial values and flags needed

  //traversing each row one by one
  $("table tr").each(function () {
    if (positionValue == 0) {
      //if no value then display row
      positionFlag = 1;
    } else if (positionValue == $(this).find("td.position").data("position")) {
      positionFlag = 1; //if value is same display row
    } else {
      positionFlag = 0;
    }

    if (homelandValue == 0) {
      homelandFlag = 1;
    } else if (homelandValue == $(this).find("td.homeland").data("homeland")) {
      homelandFlag = 1;
    } else {
      homelandFlag = 0;
    }

    if (positionFlag && homelandFlag) {
      $(this).show(); //displaying row which satisfies all conditions
    }
  });
}

$(".filter-report").on("input", function () {
    var date_from = $("#filter_date_from").val();
    var date_to = $("#filter_date_to").val();
    var companion_filter = $("#companion_filter").val()

    $("table tbody tr").each(function () {
      var row = $(this);
      var date = row.find("td").eq(2).text();
      var companion = row.find("td").eq(0).text();

      //show all rows by default
      var show = true;
      if (companion && companion != companion_filter)
         show = false
      //if from date is valid and row date is less than from date, hide the row
      if (date_from && date < date_from)
        show = false;

      //if to date is valid and row date is greater than to date, hide the row
      if (date_to && date > date_to)
        show = false;

      if (show)
        row.show();
      else
        row.hide();
    });
  });

//$(".filter-report").change(function () {
//  filter_report_function();
//});

//$("table tbody tr").show(); //intially all rows will be shown

//function filter_report_function() {
//  $("table tbody tr").hide(); //hide all rows
//
//  var companionFlag = 0;
//  var companionValue = $("#companion_filter").val();
//  var dateFlag = 0;
//  var dateFromValue = $("#filter_date_from").val();
//  var dateToValue = $("#filter_date_to").val();
//
//  //setting intial values and flags needed
//
//  //traversing each row one by one
//  $("table tr").each(function () {
//    if (companionValue == 0) {
//      companionFlag = 1;
//    } else if (companionValue == $(this).find("td.companion").data("companion")) {
//      companionFlag = 1; //if value is same display row
//    } else {
//      companionFlag = 0;
//    }
//
//    if (dateFromValue === "" || dateToValue === "") {
//      dateFlag = 1;
//    } else if (
//    (new Date(dateFromValue) <= new Date($(this).find("td.date").data("date"))) && new Date(($(this).find("td.date").data("date")) <= new Date(dateToValue))
//    ) {
//      dateFlag = 1;
//      console.log('This is message which is true.');
//    } else {
//      dateFlag = 0;
//      console.log('This is message which is false.');
//    }
//
//    if (companionFlag && dateFlag) {
//      $(this).show(); //displaying row which satisfies all conditions
//    }
//  });
//}
