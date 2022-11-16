const axios = require("axios");
const APIURL = "https://api.nytimes.com/svc";
export const requestsMixin = {
  methods: {
    getArticles(section) {
      return axios.get(
        `${APIURL}/topstories/v2/${section}.json?api-key=${process.env.VUE_APP_API_KEY}`
      );
    },
searchArticles(keyword) {
      return axios.get(
        `${APIURL}/search/v2/articlesearch.json?api-key=${process.env.VUE_APP_API_KEY}&q=${keyword}`
      );
    }
  }
};