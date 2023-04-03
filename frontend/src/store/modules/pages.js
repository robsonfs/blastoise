import axios from 'axios';

const state = {
  pages: null,
  page: null
};

const getters = {
  statePages: state => state.pages,
  statePage: state => state.page,
};

const actions = {
  async createpage({dispatch}, page) {
    await axios.post('/', page);
    await dispatch('getpages');
  },
  async getpages({commit}) {
    let {data} = await axios.get('/');
    commit('setpages', data);
  },
  async viewpage({commit}, id) {
    let {data} = await axios.get(`page/${id}`);
    commit('setpage', data);
  },
  // eslint-disable-next-line no-empty-pattern
  async updatepage({}, page) {
    await axios.patch(`page/${page.id}`, page.form);
  },
};

const mutations = {
  setpages(state, pages){
    state.pages = pages;
  },
  setpage(state, page){
    state.page = page;
  },
};

export default {
  state,
  getters,
  actions,
  mutations
};
