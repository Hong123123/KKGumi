function issue_icode() {
            var postData = new FormData();
            postData.append("user", user);
            postData.append("pwd", pwd);
            fetch(window.location.search,{
                method: "POST",
                body: postData
            }).then(response => response.json()).then(function (j){
                //console.log(j.toString());
                switch (j["code"]) {
                    case 0:
                        try {
                            window.location.href = window.location.search.split("callback=")[1].split("&")[0];
                        }catch(e) {
                            window.location.href = "/dashboard";
                        } break;
                    case 1: /* TODO*/ break;
                    case 2: break;
                }
            });
            return false;
        }