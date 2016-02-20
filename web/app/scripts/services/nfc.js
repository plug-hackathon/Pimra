'use strict';

/**
 * @ngdoc service
 * @name pimraApp.nfc
 * @description
 * # nfc
 * Service in the pimraApp.
 */
angular.module('pimraApp')
  .service('nfc', function ($resource) {
    var dump_resource = $resource('http://127.0.0.1:5000/nfc/read');
    return dump_resource;
  });
