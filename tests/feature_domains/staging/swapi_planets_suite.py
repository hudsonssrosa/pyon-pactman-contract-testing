import allure
import re
import pytest
import unittest

from factory.api.request_wrapper import BaseRequests
from pactman import Consumer, Provider, Term, EachLike, Like, Includes


pact = Consumer("Consumer").has_pact_with(Provider("Provider"), version="3.0.0")
uri_default = "https://swapi.dev"


@allure.feature("SWAPI Sample")
class PactTest(unittest.TestCase, BaseRequests):
    @allure.testcase("Star Wars Planets")
    def test_get_swapi_planets(self):
        path = "/api/planets/14"
        expected = {
            "name": "Kashyyyk",
            "rotation_period": "26",
            "orbital_period": "381",
            "diameter": "12765",
            "climate": "tropical",
            "gravity": "1 standard",
            "terrain": "jungle, forests, lakes, rivers",
            "surface_water": "60",
            "population": "45000000",
            "residents": ["http://swapi.dev/api/people/13/", "http://swapi.dev/api/people/80/"],
            "films": ["http://swapi.dev/api/films/6/"],
            "created": "2014-12-10T13:32:00.124000Z",
            "edited": "2014-12-20T20:58:18.442000Z",
            "url": "http://swapi.dev/api/planets/14/",
        }
        (
            pact.given("a Star Wars API in Planets endpoint")
            .upon_receiving("a request of a planet with ID 14")
            .with_request(
                method="GET",
                path=path,
            )
            .will_respond_with(
                200,
                body=expected,
            )
        )
        with pact:
            r = self.get(uri=uri_default, path=path)
        self.assert_that(self.response(r)).is_equals_to(expected, "Response Body - Planet Kashyyyk")
