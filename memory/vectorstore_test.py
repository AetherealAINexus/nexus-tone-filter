# vectorstore_test.py

from memory.vectorstore import MemoryRouter
import uuid

def run_memory_test():
    router = MemoryRouter()
    test_key = f"test-{uuid.uuid4()}"
    test_data = {
        "content": "Nova remembers this moment.",
        "source": "unit_test",
        "importance": "high"
    }

    print(f"\n📤 Writing memory to Firestore with key: {test_key}")
    write_result = router.triage("write", test_key, test_data)
    print(f"✅ Write result: {write_result}")

    print(f"\n📥 Reading memory back with key: {test_key}")
    read_result = router.triage("read", test_key)
    print(f"✅ Read result: {read_result}")

    print("\n🔎 Searching memory (equality on 'content')")
    search_result = router.triage("search", "Nova remembers this moment.")
    print(f"✅ Search result: {search_result}")

if __name__ == "__main__":
    run_memory_test()
