- [자바에서의 System.out.print() 줄바꿈](https://github.com/SeoMiYoung/miyoung-zone/issues/153)
- [자바 배열 초기화 기본값](https://github.com/SeoMiYoung/miyoung-zone/issues/154)
- [`=`와 `equals`](https://github.com/SeoMiYoung/miyoung-zone/issues/155)
- [오버라이딩 & 동적바인딩](https://github.com/SeoMiYoung/miyoung-zone/issues/156)
- [오버로딩](https://github.com/SeoMiYoung/miyoung-zone/issues/157)
- [추상클래스](https://github.com/SeoMiYoung/miyoung-zone/issues/159)

### ✔️ java에서의 싱글톤 패턴
클래스를 여러번 호출했을 때, 인스턴스를 하나만 생성하고, 그 다음 생성 시, 기존에 생성한 것이 있나 확인하고, 있으면 기존 것 반환 => `싱글톤`

### ✔️ swith()문
break문이 없다면, 조건을 만족한 곳~끝까지 계속 실행됨.

### ✔️ static
클래스에 딱 1개만 존재하는 필드/메서드로, 객체를 생성하지 않아도 클래스 이름으로 접근할 수 있어!
static은 클래스에 소속! (인스턴스 아님!) 

static은 클래스에 고정된 "공용 자원"이야.
객체 없이 바로 접근할 수 있고, 모든 인스턴스가 공유해서 쓰는 거다!

#### <static 변수인 count는 모든 인스턴스가 공유함>
```
class Counter {
    static int count = 0;

    Counter() {
        count++;
        System.out.println("count = " + count);
    }
}
```
```
public class Main {
    public static void main(String[] args) {
        new Counter(); // count = 1
        new Counter(); // count = 2
        new Counter(); // count = 3
    }
}
```

#### <static 메서드>
```
class MathUtil {
    static int square(int x) {
        return x * x;
    }
}
```
```
int result = MathUtil.square(5);  // ✅ 객체 생성 없이 바로 호출
```

- 단, static 메서드 안에서는 인스턴스(멤버) 변수 사용 불가! --> 그 이유는, 생성 안하고도 사용할 수 있다고 했잖아 static은? 그런데 만약에 생성해야지만 만들어지는 멤버 변수에 접근할 수 있게 하면, 뭔가 꼬이지..
- static 메서드에서는 this, super 사용 불가능!

```
static void method() {
    System.out.println(this.value); // ❌ 오류!
}
```

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

