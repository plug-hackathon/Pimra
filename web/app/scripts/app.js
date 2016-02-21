'use strict';

/**
 * @ngdoc overview
 * @name pimraApp
 * @description
 * # pimraApp
 *
 * Main module of the application.
 */
angular
  .module('pimraApp', [
    'ngAnimate',
    'ngCookies',
    'ngResource',
    'ngRoute',
    'ngSanitize',
    'ngTouch'
  ])
  .config(function ($routeProvider, $httpProvider) {

    $httpProvider.defaults.headers.post['Content-Type'] = 'application/json;';

    $routeProvider
      .when('/', {
        templateUrl: 'views/main.html',
        controller: 'MainCtrl',
        controllerAs: 'main'
      })
      .when('/nfc', {
        templateUrl: 'views/nfc.html',
        controller: 'NfcCtrl',
        controllerAs: 'nfc'
      })
      .otherwise({
        redirectTo: '/'
      });
  });
