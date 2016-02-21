'use strict';

/**
 * @ngdoc function
 * @name pimraApp.controller:NfcCtrl
 * @description
 * # NfcCtrl
 * Controller of the pimraApp
 */
angular.module('pimraApp')
  .controller('NfcCtrl', function ($scope, nfc, $http) {
    $scope.awesomeThings = [
      'HTML5 Boilerplate',
      'AngularJS',
      'Karma'
    ];

    $scope.dump = function () {
      $http.post('http://127.0.0.1:5000/nfc/read', JSON.stringify({'a': 'b'}));
    };
  });
