import { createStore } from "vuex";

import pages from './modules/pages';

export default createStore({
  modules: {
    pages
  }
});
