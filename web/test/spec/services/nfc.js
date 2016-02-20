'use strict';

describe('Service: nfc', function () {

  // load the service's module
  beforeEach(module('pimraApp'));

  // instantiate service
  var nfc;
  beforeEach(inject(function (_nfc_) {
    nfc = _nfc_;
  }));

  it('should do something', function () {
    expect(!!nfc).toBe(true);
  });

});
