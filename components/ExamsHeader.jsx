import UploadButton from "./UploadButton";

function ExamsHeader() {
  return (
    <div className="flex w-full justify-between py-4 border-b">
      <h2 className="text-3xl font-bold">My Exams</h2>
      <UploadButton />
    </div>
  );
}

export default ExamsHeader;
