- [자바에서의 System.out.print() 줄바꿈](https://github.com/SeoMiYoung/miyoung-zone/issues/153)
- [자바 배열 초기화 기본값](https://github.com/SeoMiYoung/miyoung-zone/issues/154)
- [`=`와 `equals`](https://github.com/SeoMiYoung/miyoung-zone/issues/155)
- [오버라이딩 & 동적바인딩](https://github.com/SeoMiYoung/miyoung-zone/issues/156)
- [기본 생성자와 생성자 호출 과정](https://github.com/SeoMiYoung/miyoung-zone/issues/164)
- [오버로딩](https://github.com/SeoMiYoung/miyoung-zone/issues/157)
- [추상클래스 & 인터페이스](https://github.com/SeoMiYoung/miyoung-zone/issues/159)
- [싱글톤 패턴](https://github.com/SeoMiYoung/miyoung-zone/issues/165)
- [switch문](https://github.com/SeoMiYoung/miyoung-zone/issues/166)
- [static](https://github.com/SeoMiYoung/miyoung-zone/issues/167)





### ✔️ Thread 관련 흐름
```
Thread t = new Thread(); // ❶ 스레드 객체 생성
t.start();               // ❷ 스레드 실행 시작 (run() 호출)
t.join();                // ❸ 이 스레드가 끝날 때까지 기다림
```
![image](https://github.com/user-attachments/assets/e03a35bb-a6dc-4171-b349-f334d142141c)
![image](https://github.com/user-attachments/assets/b595b158-bee1-46a3-99e4-80d5735de56a)
![image](https://github.com/user-attachments/assets/b6d2edcb-f339-4859-be0e-84b49e0dd594)
![image](https://github.com/user-attachments/assets/55f08ecf-3136-4ac6-8f34-92cda00f8106)
![image](https://github.com/user-attachments/assets/b0337a41-137a-4fb3-8283-8b8f9e11437e)
![image](https://github.com/user-attachments/assets/189b6427-7cd1-4a4b-a169-e95ee8e7d73e)

### ✔️ java에서 몫을 구하려면?
![image](https://github.com/user-attachments/assets/a641805a-69f9-4828-80d2-8b8bfe45bf80)


### ✔️ 연산자
```
public class OperatorExample {
    public static void main(String[] args) {
        // =====================
        // 1️⃣ 논리 연산 (boolean)
        // =====================
        boolean a = true;
        boolean b = false;

        System.out.println("=== 논리 연산자 ===");
        System.out.println("!a        = " + (!a));        // false
        System.out.println("a ^ b     = " + (a ^ b));      // true (다르면 true)
        System.out.println("a | b     = " + (a | b));      // true (하나라도 true면 true)

        // =====================
        // 2️⃣ 비트 연산 (정수)
        // =====================
        int x = 5;  // 0101
        int y = 3;  // 0011

        System.out.println("\n=== 비트 연산자 ===");
        System.out.println("x        = " + x);            // 5
        System.out.println("y        = " + y);            // 3
        System.out.println("x ^ y    = " + (x ^ y));      // 6 (0110)
        System.out.println("x | y    = " + (x | y));      // 7 (0111)
        System.out.println("~x       = " + (~x));         // -6 (비트 반전, 2의 보수)

        // 참고: 논리 NOT `!`은 정수에 사용할 수 없음
        // System.out.println(!x);  // ❌ 오류
    }
}
```
```
=== 논리 연산자 ===
!a        = false
a ^ b     = true
a | b     = true

=== 비트 연산자 ===
x        = 5
y        = 3
x ^ y    = 6
x | y    = 7
~x       = -6
```


