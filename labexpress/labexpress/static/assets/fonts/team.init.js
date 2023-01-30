var buttonGroups, list = document.querySelectorAll(".team-list");
function onButtonGroupClick(e) {
    "list-view-button" === e.target.id || "list-view-button" === e.target.parentElement.id ? (document.getElementById("list-view-button").classList.add("active"),
        document.getElementById("grid-view-button").classList.remove("active"),
        Array.from(list).forEach(function (e) {
            e.classList.add("list-view-filter"),
                e.classList.remove("grid-view-filter")
        })) : (document.getElementById("grid-view-button").classList.add("active"),
            document.getElementById("list-view-button").classList.remove("active"),
            Array.from(list).forEach(function (e) {
                e.classList.remove("list-view-filter"),
                    e.classList.add("grid-view-filter")
            }))
}
list && (buttonGroups = document.querySelectorAll(".filter-button")) && Array.from(buttonGroups).forEach(function (e) {
    e.addEventListener("click", onButtonGroupClick)
});
var url = "assets/json/", allmemberlist = "";
var searchMemberList = document.getElementById("searchMemberList");
searchMemberList.addEventListener("keyup", function () {
    var e = searchMemberList.value.toLowerCase();
    t = e;
    var t, e = allmemberlist.filter(function (e) {
        return -1 !== e.Name.toLowerCase().indexOf(t.toLowerCase()) || -1 !== e.Address.toLowerCase().indexOf(t.toLowerCase())
    });
    0 == e.length ? (document.getElementById("noresult").style.display = "block",
        document.getElementById("teamlist").style.display = "none") : (document.getElementById("noresult").style.display = "none",
            document.getElementById("teamlist").style.display = "block"),
        loadTeamData(e)
});
function loadTeamData(result) {
    let items = document.querySelectorAll("#team-member-list>div.col");
    items.forEach(function (e, t) {
        let id = e.id;
        var item = result.filter(x => x.IdeCompany == id);
        if (item.length == 0) {
            e.style.display = "none";
        } else {
            e.style.display = "";
        }
    })
}