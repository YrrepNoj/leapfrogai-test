"""OpenAI Compliant Threads API Router."""

from typing import List
from fastapi import HTTPException, APIRouter
from openai.types.beta import Thread, ThreadDeleted
from openai.types.beta.threads import Message
from openai.types.beta.threads import Run
from openai.types.beta.threads.runs import RunStep


router = APIRouter(prefix="/openai/v1/threads", tags=["openai/threads"])


@router.post("/")
def create_thread() -> Thread:
    """Create a thread."""
    # TODO: Implement this function
    raise HTTPException(status_code=501, detail="Not implemented")


@router.get("/{thread_id}")
def retrieve_thread(thread_id: str) -> Thread:
    """Retrieve a thread."""
    # TODO: Implement this function
    raise HTTPException(status_code=501, detail="Not implemented")


@router.post("/{thread_id}")
def modify_thread(thread_id: str) -> Thread:
    """Modify a thread."""
    # TODO: Implement this function
    raise HTTPException(status_code=501, detail="Not implemented")


@router.delete("/{thread_id}")
def delete_thread(thread_id: str) -> ThreadDeleted:
    """Delete a thread."""
    # TODO: Implement this function
    raise HTTPException(status_code=501, detail="Not implemented")


@router.post("/{thread_id}/messages")
def create_message(thread_id: str) -> Message:
    """Create a message."""
    # TODO: Implement this function
    raise HTTPException(status_code=501, detail="Not implemented")


@router.get("/{thread_id}/messages")
def list_messages(thread_id: str) -> List[Message]:
    """List all the messages in a thread."""
    # TODO: Implement this function
    raise HTTPException(status_code=501, detail="Not implemented")


@router.get("/{thread_id}/messages/{message_id}")
def retrieve_message(thread_id: str, message_id: str) -> Message:
    """Retrieve a message."""
    # TODO: Implement this function
    raise HTTPException(status_code=501, detail="Not implemented")


@router.post("/{thread_id}/messages/{message_id}")
def modify_message(thread_id: str, message_id: str) -> Message:
    """Modify a message."""
    # TODO: Implement this function
    raise HTTPException(status_code=501, detail="Not implemented")


@router.post("/{thread_id}/runs")
def create_run(thread_id: str) -> Run:
    """Create a run."""
    # TODO: Implement this function
    raise HTTPException(status_code=501, detail="Not implemented")


@router.post("/runs")
def create_thread_and_run(assistant_id: str) -> Run:
    """Create a thread and run."""
    # TODO: Implement this function
    raise HTTPException(status_code=501, detail="Not implemented")


@router.get("/{thread_id}/runs")
def list_runs(thread_id: str) -> List[Run]:
    """List all the runs in a thread."""
    # TODO: Implement this function
    raise HTTPException(status_code=501, detail="Not implemented")


@router.get("/{thread_id}/runs/{run_id}")
def retrieve_run(thread_id: str, run_id: str) -> Run:
    """Retrieve a run."""
    # TODO: Implement this function
    raise HTTPException(status_code=501, detail="Not implemented")


@router.post("/{thread_id}/runs/{run_id}")
def modify_run(thread_id: str, run_id: str) -> Run:
    """Modify a run."""
    # TODO: Implement this function
    raise HTTPException(status_code=501, detail="Not implemented")


@router.post("/{thread_id}/runs/{run_id}/submit_tool_outputs")
def submit_tool_outputs(thread_id: str, run_id: str) -> Run:
    """Submit tool outputs for a run."""
    # TODO: Implement this function
    raise HTTPException(status_code=501, detail="Not implemented")


@router.post("/{thread_id}/runs/{run_id}/cancel")
def cancel_run(thread_id: str, run_id: str) -> Run:
    """Cancel a run."""
    # TODO: Implement this function
    raise HTTPException(status_code=501, detail="Not implemented")


@router.get("/{thread_id}/runs/{run_id}/steps")
def list_run_steps(thread_id: str, run_id: str) -> List[RunStep]:
    """List all the steps in a run."""
    # TODO: Implement this function
    raise HTTPException(status_code=501, detail="Not implemented")


@router.get("/{thread_id}/runs/{run_id}/steps/{step_id}")
def retrieve_run_step(thread_id: str, run_id: str, step_id: str) -> RunStep:
    """Retrieve a step."""
    # TODO: Implement this function
    raise HTTPException(status_code=501, detail="Not implemented")