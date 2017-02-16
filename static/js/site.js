"use strict";

var app = angular.module("TakeMeThere", []);
app.controller("AngularController", function($scope) {
    var socket = io.connect(location.href + "socketio");

    $scope.results = [];
    $scope.query = "";

    $scope.search = function() {
        socket.emit("search", $scope.query);
    };

    socket.on("connect", function() {
        console.log("Connected!");
    });

    socket.on("addResult", function($result) {
        console.log("result");
        $scope.results.push($result);
        $scope.$apply();
    });
});