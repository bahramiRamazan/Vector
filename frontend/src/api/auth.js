import session from './session';

export default {
  login(username, password) {
    return session.post('/auth/login/', { username, password });
  
  },
  logout() {
    // document.location.href = "https://www.google.com/accounts/Logout?continue=https://appengine.google.com/_ah/logout?continue=http://http://127.0.0.1:8000/";

    return session.post('/auth/logout/', {});
    
  },
  createAccount(username, password1, password2, email,mobil,language_prefered) {
    return session.post('/registration/', { username, password1, password2, email, mobil, language_prefered });
  },
  changeAccountPassword(password1, password2) {
    return session.post('/auth/password/change/', { password1, password2 });
  },
  sendAccountPasswordResetEmail(email) {
    return session.post('/auth/password/reset/', { email });
  },
  resetAccountPassword(uid, token, new_password1, new_password2) { // eslint-disable-line camelcase
    return session.post('/auth/password/reset/confirm/', { uid, token, new_password1, new_password2 });
  },
  getAccountDetails() {
    return session.get('/auth/user/');
  },
  updateAccountDetails(data) {
    return session.patch('/auth/user/', data);
  },
  verifyAccountEmail(key) {
    return session.post('/registration/verify-email/', { key });
  },
};
