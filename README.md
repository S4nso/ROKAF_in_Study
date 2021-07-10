# ROKAF_in_Study

***

### 군대 안에서 활동하기.

<script>
var dday = new Date("January 11, 2023, 0:00:00").getTime();

setInterval(function() {
  var today = new Date().getTime();
  var gap = dday - today;
  var day = Math.ceil(gap / (1000 * 60 * 60 * 24));
  var hour = Math.ceil((gap % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
  var min = Math.ceil((gap % (1000 * 60 * 60)) / (1000 * 60));
  var sec = Math.ceil((gap % (1000 * 60)) / 1000);

  document.getElementById("count").innerHTML = "D-DAY까지 " + day + "일 " + hour + "시간 " + min + "분 " + sec + "초 남았습니다.";
}, 1000);
</script>

**+ 군 장병 SW 해커톤 준비 中 (국방 오픈소스 아카데미)**


https://www.goorm.io/         // 구름 IDE

https://programmers.co.kr/    // 프로그래머스 1일1문제 이상

https://www.acmicpc.net/      // 백준 1일 1문제 이상


